import sys
import json

from .telegram import Telegram


def print_line(s):
    sys.stdout.write(f'{s}\n')
    sys.stdout.flush()


def read_line():
    try:
        line = sys.stdin.readline().strip()
        if not line:
            sys.exit(3)
        return line
    except KeyboardInterrupt:
        sys.exit()


def auth():
    tg = Telegram()
    tg.auth()


def poll():
    tg = Telegram()

    print_line(read_line())
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)
        print_line(prefix + json.dumps(tg.unread() + j))


if __name__ == '__main__':
    poll()
