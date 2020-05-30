# -*- coding: utf-8 -*-
from coins.prices import get_price_from_aicoin

import logging

def usdt_price_command(update, context):
    """
    get usdt price from aicoin

    """
    coin_info = get_price_from_aicoin("usdt", "usdtcnyt:bitasset")
    html_text = u"--------------\n"
    html_text += u"price now: {0}\n".format(coin_info["last"] or -1)
    html_text += u"--------------\n"
    context.bot.send_message(chat_id=update.message.chat_id, text=html_text)