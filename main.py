# -*- coding: utf-8 -*-


import logging

from telegram.ext import Updater

from handlers import error_handler, usdt_handler

from timer import price_notify

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def main():
    """
    Create a telegram bot

    :return:
    """

    updater = Updater(
        token='',
        use_context=True
    )
    dispatcher = updater.dispatcher
    dispatcher.add_handler(usdt_handler)
    dispatcher.add_error_handler(error_handler)
    updater.job_queue.run_repeating(price_notify, interval=60, first=0)
    updater.start_polling(poll_interval=3.0)
    updater.idle()


if __name__ == "__main__":
    main()
