# Customer Review

This app uses the public [Amazon Customer Reviews Dataset](https://registry.opendata.aws/amazon-reviews/). Ingester is a Celery app that ingest the dataset `amazon_reviews_us_Furniture_v1_00.tsv.gz` into MySQL DB. App is built with Flask and Swagger that provides an api to query the `customer_review` table.

# Local Development
* to docker-compose up all the services, and start the ingesting task:
```bash
make local
```
* to check the ingestion task status:
```bash
http://localhost:5555/
```
* app healthcheck:
```bash
http://0.0.0.0:8000/healthcheck
```
* swagger ui of the api:
```bash
http://0.0.0.0:8000/ui
```
* to run test locally
```bash
make test
```
