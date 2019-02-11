local:
	docker-compose up -d --build
	sleep 20
	curl -X POST -d '{"args": ["amazon_reviews_us_Furniture_v1_00.tsv.gz"]}' http://localhost:5555/api/task/async-apply/ingester.tasks.ingest_data_to_db

clean:
	docker-compose down --remove-orphans || true

test: clean
	docker-compose build
	docker-compose run --rm app pytest -svv --cov=app --cov-report term-missing
	docker-compose run --rm ingester pytest -svv --cov=ingester --cov-report term-missing
