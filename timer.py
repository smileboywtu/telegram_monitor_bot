# -*- coding: utf-8 -*-


"""

timer task to know

"""

import logging
from collections import defaultdict
from coins.prices import get_price_from_aicoin, get_usdt_price_banner_from_aicoin

user_chat_id = "-1001336120946"


percent = 0.0099 # 10%
history_cache = defaultdict(float)

def price_notify(context):
    """
    货币价格提醒，盈亏提醒
    """
    # coin_info = get_price_from_aicoin("usdt", "usdtcnyt:bitasset")
    coin_info = get_usdt_price_banner_from_aicoin()
    # coin_name, coin_price = coin_info["coin_show"], float(coin_info["last"]*7.04)
    coin_name, coin_price = "usdt-cny", float(coin_info["last"])
    logging.info("current: {0}, old: {1}".format(coin_price, history_cache[coin_name])) 
    if coin_name not in history_cache:
        history_cache[coin_name] = coin_price
        message = u"当前价格(当前)： {0}".format(coin_price)
    else:
        old_price = history_cache[coin_name]
        state = 1 if coin_price > old_price else 0
        if abs(old_price - coin_price) >= percent:
            message = u"当前价格({0}): {1}".format( "上涨" if state else "下跌",coin_price)
        else:
            message = None
        history_cache[coin_name] = coin_price
    
    if message:
        context.bot.send_message(
            chat_id=user_chat_id,
            text=message
        )