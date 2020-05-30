# -*- coding: utf-8 -*-


import logging

logger = logging.getLogger("bot")


def error_handler(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
