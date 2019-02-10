import logging
from celery import Celery, Task
from ingester import config as cfg
from ingester.aws import download_file
from ingester.db import load_review
from ingester.utils import tmp_dir


logger = logging.getLogger(__name__)


app = Celery("tasks", broker=cfg.CELERY.BrokerUrl, backend=cfg.CELERY.ResultBackend)

app.conf.update(
    result_expires=10,
    beat_schedule={
    })


class BaseTask(Task):
    abstract = True

    def __call__(self, *args, **kwargs):
        super(BaseTask, self).__call__(*args, **kwargs)
        logger.info(f'Ingestion started')

    def on_success(self, retval, task_id, args, kwargs):
        logger.info(f'Ingestion succeeded')

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.info(f'Ingestion failed')


@app.task(name='ingester.tasks.ingest_data_to_db', base=BaseTask, bind=True)
def ingest_data_to_db(self, key) -> None:
    with tmp_dir() as working_dir:
        filepath = download_file(key, working_dir)
        load_review(filepath)
