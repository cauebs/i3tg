import os

from getpass import getpass

from telethon import TelegramClient
from telethon.errors.rpc_errors_401 import SessionPasswordNeededError

from . import config


class Telegram:
    def __init__(self):
        os.chdir(config.CONFIG_DIR)
        self.client = TelegramClient('i3tg', config.API_ID, config.API_HASH)
        self.client.connect()

    def auth(self):
        self.client.sign_in(phone=config.PHONE_NUMBER)
        try:
            self.client.sign_in(code=int(input('Code: ')))
        except SessionPasswordNeededError:
            self.client.sign_in(password=getpass('Pass: '))

    def unread(self):
        dialogs, entities = self.client.get_dialogs()

        unread_count = sum(d.unread_count
                           for d in dialogs
                           if config.COUNT_SILENCED or
                           not (d.notify_settings.silent or
                                d.notify_settings.mute_until))

        mention_count = sum(d.unread_mentions_count
                            for d in dialogs)

        output = []

        if unread_count:
            output.append({
                'name': 'tg_unread',
                'color': config.UNREAD_COLOR,
                'full_text': config.UNREAD_FORMAT.format(unread_count),
            })

        if mention_count:
            output.append({
                'name': 'tg_mentions',
                'color': config.MENTION_COLOR,
                'full_text': config.MENTION_FORMAT.format(mention_count),
            })

        return output
