from time import sleep

from celery import Celery

appCelery = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/1')


@appCelery.task
def send_msg(x, y):
    sleep(x)
    print(x+y)
    return x + y
