import json
from os import environ
from pathlib import Path


CONFIG_DIR = Path(environ['XDG_CONFIG_HOME'], 'i3tg')

with open(CONFIG_DIR / 'config.json') as f:
    config = json.load(f)

API_ID = config['api_id']
API_HASH = config['api_hash']
PHONE_NUMBER = config['phone_number']

UNREAD_COLOR = config.get('unread_color', '#FFFFFF')
MENTION_COLOR = config.get('mention_color', '#FF0000')

UNREAD_FORMAT = config.get('unread_format', 'unread messages: {}')
MENTION_FORMAT = config.get('mention_format', 'mentions: {}')

COUNT_SILENCED = config.get('count_silenced', False)
