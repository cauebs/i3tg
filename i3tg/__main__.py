import sys
import json

from threading import Thread

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
    print_line(read_line())
    print_line(read_line())

    tg = None
    while not tg:
        try:
            tg = Telegram()
        except:
            print_line(read_line())

    Thread(target=tg.poll).start()

    while True:
        prefix, line = '', read_line()
        if line.startswith(','):
            prefix, line = ',', line[1:]

        j = json.loads(line)
        output = tg.unread + j
        output = prefix + json.dumps(output)

        print_line(output)


if __name__ == '__main__':
    poll()
