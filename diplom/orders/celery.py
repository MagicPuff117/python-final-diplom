
import os

from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diplom.settings')
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = celery = Celery('diplom',
                broker='sqla+sqlite:///' + os.path.join(basedir, 'celery.db'),
                backend='db+sqlite:///' + os.path.join(basedir, 'celery_results.db'))


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')