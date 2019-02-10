local: clean
	docker-compose up -d --build
	sleep 20
	curl -X POST -d '{"args": ["amazon_reviews_us_Furniture_v1_00.tsv.gz"]}' http://localhost:5555/api/task/async-apply/ingester.tasks.ingest_data_to_db

clean:
	docker-compose down --remove-orphans || true

test:
	command:=pytest -svv --cov=app --cov-report term-missing
