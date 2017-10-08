i3tg
====
Telegram unread count with i3status


Installation
------------
```
pipsi install git+https://github.com/cauebs/i3tg#egg=i3tg
```

Configuration
-------------
1. Create an app at https://my.telegram.org/
2. Create a file at `$XDG_CONFIG_HOME/i3tg/config.json` and fill it with your credentials (id, hash and phone number). Other preferences are optional

Example configuration:
```json
{
    "api_id": 000000,
    "api_hash": "0123456789abcdef0123456789abcdef",
    "phone_number": "+1234567890",

    "unread_color": "#FFFFFF",
    "mention_color": "#FF0000",

    "unread_format": "unread messages: {}",
    "mention_format": "mentions: {}",

    "count_silenced": false
}
```

Usage
-----
First, you need to authorize it with
```
i3tg-auth
```
It will ask you for the code you receive on Telegram and your password if you've configured two-steps authentication.

After you're done, just change the `status_command` in the "bar" section of your i3 configuration file:
```
bar {
    status_command i3status | i3tg-poll
}
```
Restart i3 and it should be working.

It should work with anything which output is in the JSON format accepted by the i3bar.
