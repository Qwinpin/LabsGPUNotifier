import functools
import socket
import time

import config


def send_note(text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((config.HOST, config.PORT))
        s.sendall(text)


def notifier(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        start = time.time()

        print('Server will be notified about this task finish')
        result = func(*args, **kwargs)

        end = time.time()
        send_note(b"Task finished in %b sec" % str(end - start).encode())

        return result

    return wrap


@notifier
def wop():
    print('I do something')
