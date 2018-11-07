import functools
import socket


HOST = '192.168.0.245'
PORT = 5005


def send_note(text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(text)


def notifier(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        print('Server will be notified about this task finish')
        result = func(*args, **kwargs)
        send_note(b'Task finished')

        return result

    return wrap


@notifier
def wop():
    print('I do something')


wop()