# -*- coding: utf-8 -*-


from telegram.ext import CommandHandler

from handlers.commands import usdt_price_command
from handlers.errors import error_handler

usdt_handler = CommandHandler("usdt", usdt_price_command)
