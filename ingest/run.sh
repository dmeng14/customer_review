#!/bin/bash

if [ "$RUN_MODE" == 'worker' ]; then
  echo "STARTING INGESTER WORKER WITH QUEUES $queues"
  celery -A ingester.tasks -Q celery worker --loglevel=ERROR --concurrency 1
elif [ "$RUN_MODE" == 'local' ]; then
  echo "STARTING INGESTER LOCAL WORKER"
  celery -A ingester.tasks -Q celery worker --loglevel=INFO --concurrency 1
elif [ "$RUN_MODE" == 'flower' ]; then
  echo "STARTING INGESTER FLOWER"
  celery flower -A ingester.tasks --port=5555
else
  "RUN_MODE $RUN_MODE blank/not supported"
  exit 1
fi
