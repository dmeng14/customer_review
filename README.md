# customer_review

This app uses the public Amazon Customer Reviews Dataset. Ingester is a celery app that ingest the dataset `amazon_reviews_us_Furniture_v1_00.tsv.gz` into a MySQL DB. App is an api that can query the reviews.

# local development
1. to docker-compose up all the services, and start the ingesting task:
```bash
make local
```
1. to check ingestion task status:
```bash
http://localhost:5555/
```
1. to check app health:
```bash
http://0.0.0.0:8000/healthcheck
```
1. swagger ui of the api:
```bash
http://0.0.0.0:8000/ui
```
1. to run test locally
```bash
make test
```
