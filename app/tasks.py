
from celery import shared_task
from instanew2 import Insta
from dm import sendDM

from .models import Account


@shared_task
def add(x, y):
    return x + y



@shared_task
def create_account(d, proxy):
    a = Insta(d, proxy)
    a.generate()
    print('--------- task username', a.CREDS['username'])
    print('--------- task password', a.CREDS['password'])

    if a.verified:
        account = Account()
        account.username = a.CREDS['username']
        account.password = a.CREDS['password']
        account.save()


@shared_task
def send_direct_message(data):
    sendDM(data.get('username'), data.get('message'), data.get('sender'), data.get('password'))