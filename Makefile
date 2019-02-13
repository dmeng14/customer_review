local: clean
	docker-compose up -d --build
	echo 'waiting for db to initiate'
	sleep 20
	curl -X POST -d '{"args": ["amazon_reviews_us_Furniture_v1_00.tsv.gz"]}' http://localhost:5555/api/task/async-apply/ingester.tasks.ingest_data_to_db

clean:
	docker-compose down --remove-orphans || true

unit-test: clean
	docker-compose build
	docker-compose run --rm app pytest test/unit --cov=app --cov-report term-missing
	docker-compose run --rm ingester pytest -svv --cov=ingester --cov-report term-missing

integration-test: local
	echo 'ingesting data for integration test'
	sleep 60
	docker-compose run --rm app pytest test/integration --cov=app --cov-report term-missing

test: unit-test integration-test
