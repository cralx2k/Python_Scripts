# -*- coding: utf-8 -*-
"""
Logger - Carlos
"""

import logging
import os
import sys

#Color
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        GREEN = ""
        YELLOW = ""
        RED = ""
        RESET = ""

    class Style:
        RESET_ALL = ""

#Python 2.7
if sys.version_info[0] == 2:
    import __builtin__ as builtins
else:
    import builtins


class LogTemplate:
    def __init__(self, log_dir="logs", log_file="logfile.log"):
        self.log_dir = log_dir
        self.log_file = log_file
        self.logger = self.setup_logger()

    def setup_logger(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        log_path = os.path.join(self.log_dir, self.log_file)
        logger = logging.getLogger("CustomLogger")
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(file_format)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger

    def log_info(self, message):
        print(Fore.GREEN + "INFO: " + Style.RESET_ALL + message)
        self.logger.info(message)

    def log_warning(self, message):
        print(Fore.YELLOW + "WARNING: " + Style.RESET_ALL + message)
        self.logger.warning(message)

    def log_error(self, message):
        print(Fore.RED + "ERROR: " + Style.RESET_ALL + message)
        self.logger.error(message)


if __name__ == "__main__":
    log = LogTemplate()

    log.log_info("This is an info message.")
    log.log_warning("This is a warning message.")
    log.log_error("This is an error message.")
