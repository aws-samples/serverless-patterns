up:
	docker compose up --build --remove-orphans -d

up-int:
	docker compose up --build --remove-orphans

bash:
	docker compose exec app sh

deploy:
	docker compose exec app sh -c 'npm run deploy'

destroy:
	docker compose exec app sh -c 'npm run destroy'
