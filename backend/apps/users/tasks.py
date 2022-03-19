from celery import shared_task

@shared_task(name="nametasks")
def hello_(name):
    return 'hola'+name